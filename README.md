venv\Scripts\activate

To run api tests locally: 
behave api_features -f behave_html_formatter:HTMLFormatter -o api_features/reports/behave_report.html

To run ui tests locally:
behave ui_features -f behave_html_formatter:HTMLFormatter -o ui_features/reports/behave_report.html