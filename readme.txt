# lunatech-qa-equittime-assessment-template

Please use this readme as your project's readme. You can find instructions for
the assignment in the [`INSTRUCTIONS.md`](INSTRUCTIONS.md) file.

Once the tests are completed, reports will generated using the following command <br>
behave -f allure_behave.formatter:AllureFormatter -o AutomationTestReports/ <Absoulte path to where feature files are available> <br>
Above command will generate reports in json format <br>
To save and review the reports in html use command "allure serve <Absolute path to reports folder>" <br>

Packages required for this project includes: <br>
allure_behave <br>
allure-commandline to generate html reports <br>
Set path of allure-commandline in environment variables <br>
Set path of webdrivers (Chrome, firefox) in environment variables <br>