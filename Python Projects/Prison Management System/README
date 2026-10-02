# Prison Management System

A Prison Management System built with Python using Object-Oriented Programming and JSON file storage.

This is a learning project focused on building a multi-file Python application while practicing OOP, JSON, file handling, exception handling, input validation, and program design.

The project is still under development.

## Current Features

Prisoner registration currently stores:

- Prisoner ID
- Full name
- Age
- Gender
- Date of birth
- Place of birth
- Arrest date
- Arrest city
- Arrest state
- Crime committed
- Crime description
- Sentence length
- Release date
- Security classification
- Current status
- Cell number
- Number of incidents

Prisoner IDs are generated automatically in a format such as SV-38408.

The program checks existing prisoner records before accepting a generated ID to reduce the chance of duplicate IDs.

Worker registration currently stores:

- Worker ID
- Full name
- Age
- Gender
- Occupation
- Security level
- Active status

Worker IDs are automatically generated in a format such as WR-48291.

## Worker Security Levels

The system currently supports four worker security levels:

Level 1 - Support Staff

Level 2 - Guards / Registration Officers

Level 3 - Warden

Level 4 - Administrator

Security levels are currently stored with worker records.

Actual permission restrictions and authentication have not been implemented yet.

## Prisoner Security Classification

Prisoners can currently be assigned a security classification from 1 to 4:

1 - Low Security

2 - Medium Security

3 - High Security

4 - Maximum Security

This will later be used for systems such as cell assignment and prisoner movement restrictions.

## JSON Storage

The system uses JSON files to permanently store prisoner and worker records.

Current data files:

data/prisoners.json

data/workers.json

When a prisoner or worker is registered, the program creates an object from the appropriate class.

The object's to_dict() method converts its information into a dictionary.

That dictionary is then added to the existing records and saved into the correct JSON file.

Because of this, registered information is still available after the program is closed and opened again.

## Project Structure

Prison Management System/

main.py

prisoner.py

worker.py

utils.py

data/

prisoners.json

workers.json

## main.py

main.py currently contains the main program menu.

Current options are:

1. Register Prisoner

2. View Prisoners

3. Register New Worker

4. View Workers

0. Exit

It also loads prisoner and worker records from JSON so saved information can be viewed after restarting the program.

## prisoner.py

prisoner.py contains the Prisoner class.

The Prisoner class currently handles prisoner information such as identity, arrest information, crimes, sentence information, security classification, status, cell number, and incident count.

The file also handles prisoner registration, unique prisoner ID generation, input validation, conversion of Prisoner objects into dictionaries, and saving records into prisoners.json.

## worker.py

worker.py contains the Worker class.

The Worker class currently handles worker information, occupation, security level, active status, activation, deactivation, and conversion of Worker objects into dictionaries.

The file also handles worker registration, unique worker ID generation, input validation, and saving records into workers.json.

## utils.py

utils.py contains reusable functions for loading and saving JSON data.

load(file_path) reads information from a JSON file.

save(file_path, data) writes information into a JSON file.

Using these functions prevents the same JSON loading and saving code from being repeated in every file.

## Input Validation

The project currently performs validation on several inputs.

Numeric fields such as age, worker security level, and prisoner security classification use try and except to prevent invalid text input from crashing the program.

Worker security levels must be between 1 and 4.

Prisoner security classifications must also be between 1 and 4.

The currently supported gender values are male and female.

Important fields such as names, gender, occupation, arrest information, crime information, and sentence information cannot be left empty.

Workers must be at least 18 years old.

## Bugs Fixed

Data loss after restarting the program was fixed by adding JSON persistence.

Missing JSON files are handled using FileNotFoundError so the program can start with an empty list instead of crashing.

Empty or invalid JSON files are handled using JSONDecodeError.

Random prisoner and worker IDs are checked against existing records before being accepted to prevent duplicate IDs.

Invalid numeric input no longer crashes the program because numeric fields are protected using try and except.

Security levels outside the range of 1 to 4 are rejected.

Prisoner security classifications outside the range of 1 to 4 are rejected.

Underage workers cannot be registered.

Invalid gender values are rejected.

Important required fields cannot be saved while empty.

## Known Issues

Date validation is currently basic.

The program mainly checks the length of date input, so invalid values can still pass if they have the expected number of characters.

Proper date validation will be added later.

JSON storage is suitable for the current learning project, but it would not be suitable for a large system with many users editing records at the same time.

A database may be introduced later.

Authentication has not been implemented yet.

Workers currently have security levels, but those levels do not yet restrict access to different parts of the program.

## Planned Features

Planned features include:

- Worker login system
- Password authentication
- Permission system
- Security-level restrictions
- Cell management
- Cell creation
- Cell capacity
- Cell security levels
- Prisoner cell assignment
- Prisoner transfers
- Incident management
- Incident history
- Visitor management
- Court records
- Prisoner property storage
- Prisoner movement history
- Warden controls
- Administrator controls
- Audit logs
- Worker activation and deactivation management
- Prisoner search by ID
- Worker search by ID
- Better date validation
- Prisoner release management

## Current Development Status

Completed:

- Prisoner registration
- Worker registration
- JSON persistence
- Unique ID generation
- Input validation
- Main CLI menu
- Worker security level storage
- Prisoner security classification

Not completed yet:

- Authentication
- Permissions
- Cell management
- Incident management
- Visitor management
- Court records
- Administration panel

## Purpose

This project is being built mainly to practice:

- Python
- Object-Oriented Programming
- JSON
- File handling
- Exception handling
- Input validation
- Data structures
- Multi-file projects
- Program design

The project will continue to grow as more features and Python concepts are added.
