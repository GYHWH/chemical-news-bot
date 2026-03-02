# companies_updater.py

class CompaniesUpdater:
    def __init__(self, database):
        self.database = database

    def add_company(self, name, details):
        """Add a new chemical company to the database."""
        # Code to add company details to the database
        print(f'Company {name} added to database.')

    def update_company(self, company_id, new_details):
        """Update the details of an existing company."""
        # Code to update company details in the database
        print(f'Company {company_id} updated to new details.')

    def remove_company(self, company_id):
        """Remove a chemical company from the database."""
        # Code to remove company from database
        print(f'Company {company_id} removed from database.')

    def list_companies(self):
        """List all chemical companies in the database."""
        # Code to list companies
        print('Listing all companies...')
        # This would return a list of companies
