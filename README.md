# CS340-Client-Server-Development
How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?
--
Programs are made to be maintainable, readable, and adaptable by 1) avoiding hardcoded values, 2) using generic naming conventions, and 3) handling exceptions. The CRUD Python module included in this repository passes a user's login information for database access as parameters rather than literal values. Variables are given generic names like "query" to indicate their foundational purposes, regardless of specific database information. The class itself is given the generic name MongoDB_CRUD to convey it's use for CRUD operations on any MongoDB database. Creating the module with these qualities in mind made it reusable for several assignments in this course. In the future, it could be used with different databases and dashboards, truly making it the foundation for Controller functionality.

How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?
--


What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?
--
