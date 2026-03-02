class CompaniesUpdater:
    def __init__(self):
        self.companies = []

    def add_company(self, company_name):
        if company_name not in self.companies:
            self.companies.append(company_name)
            return f"{company_name} added."
        else:
            return f"{company_name} already exists."

    def get_companies(self):
        return self.companies

# Example usage
if __name__ == "__main__":
    updater = CompaniesUpdater()
    print(updater.add_company("Company A"))
    print(updater.add_company("Company B"))
    print(updater.add_company("Company A"))  # Should indicate that it already exists
    print(updater.get_companies())
