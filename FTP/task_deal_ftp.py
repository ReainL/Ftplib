#!/usr/bin/env python3.5
# encoding: utf-8
"""
Created on 18-4-26
@title: 'FTP文件上传下载'
@author: Xusl
"""
import os
import datetime
import logging.config

from ftplib import FTP
from Ftplib.settings import log_home, ftp_param, local_data_home, sys_flag_dps
from Ftplib.common.log import get_log_config, insert_sys_log
from Ftplib.common.get_conn import get_conn


log_name = 'ftp.log'
log_file = os.path.join(log_home, log_name)
log_config = get_log_config(log_file)
logging.config.dictConfig(log_config)
logger = logging.getLogger(__name__)


def _escape(file_name):
    """
    FTP服务器文件中有分隔符,所以要替换分隔符
    """
    file_path = _get_file_pre()
    src = os.path.join(file_path, file_name)
    desc = src + '.new'
    with open(desc, mode='w', encoding='utf-8') as out:
        for line in open(src, mode='r', encoding='utf-8'):
            line = line.replace('\\', '|')
            line = line.replace('^!', '\t')
            out.write(line)
    return desc


def _get_ftp():
    """
    获取ftp连接
    :return:
    """
    ftp = FTP()
    ftp.encoding = 'utf-8'
    ftp.connect(ftp_param['host'], ftp_param['port'])
    ftp.login(ftp_param['user'], ftp_param['pwd'])
    return ftp


def _get_files():
    """
    需要下载的文件
    :return:
    """
    n = datetime.datetime.now()
    s_date = n.strftime("%Y%m%d")
    file_1 = 'ftp_' + s_date + '.txt'
    ok_1 = 'ftp_' + s_date + '.ok'
    return file_1, ok_1


def _get_file_pre():
    """
    创建文件目录
    :return:
    """
    file_path = os.path.join(local_data_home, 'ftp')
    if not os.path.exists(file_path):
        os.makedirs(file_path, exist_ok=True)
    return file_path


def _get_full_files():
    """

    :return:
    """
    file_1, ok_1 = _get_files()
    file_path = _get_file_pre()
    full_file_1 = os.path.join(file_path, file_1)
    full_ok_1 = os.path.join(file_path, ok_1)
    return full_file_1, full_ok_1


def download():
    """
    下载文件
    :return:
    """
    func_name = "下载文件"
    logger.debug('start %s' % func_name)
    ftp = _get_ftp()
    logger.debug(ftp.getwelcome())
    ftp.cwd(ftp_param['NC'])
    nlst = ftp.nlst()
    file_1, ok_1 = _get_files()
    full_file_1, full_ok_1 = _get_full_files()
    if file_1 in nlst and ok_1 in nlst:
        ftp.retrbinary('RETR ' + file_1, open(full_file_1, 'wb').write)
        ftp.retrbinary('RETR ' + ok_1, open(full_ok_1, 'wb').write)
    else:
        logger.error('文件下载失败')
        raise Exception('文件下载失败')


def copy_to_db(conn, full_file, table_name):
    """
    数据文件导入
    :param conn:
    :param full_file:
    :param table_name:
    :return:
    """
    # 数据文件导入
    sql = "TRUNCATE TABLE %s" % table_name
    with conn.cursor() as cur:
        cur.execute(sql)
    with conn.cursor() as cur:
        with open(full_file, mode='r', encoding='utf-8') as fileObj:
            cur.copy_from(fileObj, table_name, null='NULL')


def deal():
    """
    NC系统数据下载和导入
    :return:
    """
    func_name = "FTP数据下载和导入"
    logger.info("start %s" % func_name)
    conn = None
    try:
        conn = get_conn(sys_code=sys_flag_dps)
        download()
        file_1, ok_1 = _get_files()
        desc_1 = _escape(file_1)
        logger.debug(desc_1)
        with conn:
            # 将数据存入数据库
            copy_to_db(conn, desc_1, 'ftp.')
    except Exception as e:
        logger.error(e)
        log_content = {
            'log_type': 'etl',
            'log_level': 'error',
            'msg': 'Ftp系统数据下载和导入: ' + str(e),
            'create_date': datetime.datetime.now(),
            'create_user': 'cron',
        }
        insert_sys_log(log_content)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    deal()
