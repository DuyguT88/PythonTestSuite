It is an automated UI and API Testing Framework, hosted on GitHub, which utilizes Python, Selenium, and Cucumber to offer advanced testing solutions.

The selection of these particular tests for the API (Swagger Petstore) and UI (UI Testing Playground) scenarios was based on common and essential features that should be tested in any application with similar functionality. Here's the reasoning for why each of these tests was considered important:

API Tests for Swagger Petstore
https://petstore.swagger.io/

Add a New Pet (POST /pet):

Importance: Adding new records or entities is a core feature of most applications. It's crucial to verify that the system can handle new data entries correctly.
Use Case: This test ensures that the API endpoint correctly accepts data, assigns new IDs, and provides appropriate validation feedback.
Update an Existing Pet (PUT /pet):

Importance: Updating existing records is essential for data integrity and user satisfaction. Users must be able to update information without creating duplicate records or errors.
Use Case: Verifies that the API handles updates by modifying only relevant fields and that the data changes reflect immediately.
Delete a Pet (DELETE /pet/{petId}):

Importance: Deletion helps maintain data accuracy and allows users to remove obsolete records.
Use Case: Tests whether an existing record can be safely removed from the system and confirms that the pet is no longer retrievable.
UI Tests for UI Testing Playground
http://www.uitestingplayground.com/ (UI)

Verify Text Input Functionality and Button Enablement:

Importance: Form input and buttons are fundamental to user interactions. Testing text input ensures that the UI accepts and processes user input correctly, while button enablement ensures the logic for controlling interactive elements works as intended.
Use Case: Assures that data entry and form submission work without issues, which directly impacts usability.
Verify Table Pagination and Data Sorting:

Importance: Pagination and sorting are crucial for providing a good user experience in data-heavy applications. Sorting ensures that data is displayed in the desired order, while pagination enables users to browse data more efficiently.
Use Case: Confirms that the UI allows users to navigate through large datasets and presents data in the expected order.
Verify Asynchronous Content Loading with AJAX:

Importance: Many modern web applications rely on AJAX to fetch or update data asynchronously. This allows the UI to be dynamic and responsive, improving user engagement.
Use Case: Verifies that data is fetched and displayed correctly in the UI after asynchronous requests, preventing user confusion due to partial or missing information.
Overall Importance
These tests cover a range of common scenarios that are essential to the functionality of both APIs and web interfaces. Ensuring that these areas work as intended helps detect issues early and ensures the fundamental features of an application deliver value and a consistent user experience.

To run api tests locally:
(venv\Scripts\activate)
behave api_features -f behave_html_formatter:HTMLFormatter -o api_features/reports/behave_report.html

To run ui tests locally:
behave ui_features -f behave_html_formatter:HTMLFormatter -o ui_features/reports/behave_report.html

Downloading Test Result Reports in CI To download test result reports in CI, begin by clicking on 'Actions.' Next, choose a specific workflow. You will find the option to download 'Artifacts' at the bottom of the workflow page.

