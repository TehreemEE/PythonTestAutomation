# PythonTestAutomation
# Instructions for setting the test environments
# Unit Test framework is used with POM and Behave

Once the tests are completed, reports will generated using the following command
behave -f allure_behave.formatter:AllureFormatter -o AutomationTestReports/ <Absoulte path to where feature files are available>
Above command will generate reports in json format
To save and review the reports in html use command "allure serve <Absolute path to reports folder>" 

Packages required for this project includes: 
allure_behave 
allure-commandline to generate html reports 
Set path of allure-commandline in environment variables 
Set path of webdrivers (Chrome, firefox) in environment variables 
