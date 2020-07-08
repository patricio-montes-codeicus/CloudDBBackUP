from Commons.app_config import APPConfig

appConfig = APPConfig()
appConfig2 = APPConfig()
print (appConfig is appConfig2)
print("DriverSQL:" + appConfig.driver_sql)