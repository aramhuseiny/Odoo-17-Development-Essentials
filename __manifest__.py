{
"name": "Library Management",
"summary": "Manage library catalog and book lending.",
"author": "Hedi",
"license": "AGPL-3",
"website": "https://example.com",
"category": "Services/Library",
"version": "17.0.1.0.0",
"depends": ["base"],
"application": True,
"data":[
    "security/library_security.xml",
    "security/ir.model.access.csv",
    "views/book_view.xml",
    "views/library_menu.xml",
    "views/book_list_template.xml"
],
"license":"AGPL-3",
"application": True,
"installable": True
}