DROP TABLE IF EXISTS web.sys_log;
CREATE TABLE web.sys_log
(
  id bigint NOT NULL,
  log_type character varying(32),
  log_level character varying(32),
  msg text,
  create_date timestamp default now(),
  create_user character varying(64),
  PRIMARY KEY (id)
);
COMMENT ON TABLE web.sys_log IS '系统日志表';
COMMENT ON COLUMN web.sys_log.id IS 'ID';
COMMENT ON COLUMN web.sys_log.log_type IS '日志类型';
COMMENT ON COLUMN web.sys_log.log_level IS '日志层级';
COMMENT ON COLUMN web.sys_log.msg IS '日志内容';
COMMENT ON COLUMN web.sys_log.create_date IS '创建日期';
COMMENT ON COLUMN web.sys_log.create_user IS '创建人';


DROP TABLE IF EXISTS ftp.emp_info;
CREATE TABLE ftp.emp_info
(
  id bigint,  -- ID
  emp_no character varying(12), -- 人员号
  gender character varying(1), -- 性别
  cust_name character varying(128), -- 名称
  create_date timestamp without time zone, -- 创建日期

);
COMMENT ON TABLE ftp.emp_info IS '人员信息表';
COMMENT ON COLUMN ftp.emp_info.id IS 'id';
COMMENT ON COLUMN ftp.emp_info.emp_no IS '人员号';
COMMENT ON COLUMN ftp.emp_info.gender IS '性别';
COMMENT ON COLUMN ftp.emp_info.emp_name IS '名称';
COMMENT ON COLUMN ftp.emp_info.create_date IS '创建日期';

