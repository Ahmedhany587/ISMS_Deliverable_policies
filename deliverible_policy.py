import openai
import os

from dotenv import load_dotenv
import os

load_dotenv()  # This loads the environment variables from the .env file

openai_api_key = os.getenv('OPENAI_API_KEY')

class InformationSecurityTool:
 

  def save_to_txt(self, information, file_path):
        with open(file_path, "w") as file:
            for question, answer in information.items():
                file.write(f"{question}\n{answer}\n\n")

  

  def gather_information(self):
    information = {}
    print("Information Security Policies and Procedures Gathering Tool")
    print("--------------------------------------------------------")

    information['Company/Organization Name'] = input("1) Company/Organization Name: ")
    information['Industry'] = input("2) Industry: ")
    information['Standard you want to apply, If you do not know write N/A'] = input("3) Standard you want to apply, If you do not know write N/A: ")

    # New Questions
    information['No. of Geographic Locations considered for the Audit'] = input("4) No. of Geographic Locations considered for the Audit: ")
    information['No. of Offices in Each Location considered for the Audit'] = input("5) No. of Offices in Each Location considered for the Audit: ")
    information['No. of Divisions/Departments considered for the Audit'] = input("6) No. of Divisions/Departments considered for the Audit: ")
    information['No. of Employees in each Department considered for the Audit'] = input("7) No. of Employees in each Department considered for the Audit: ")
    information['How many Data Centers do you have? Kindly mention their location.'] = input("8) How many Data Centers do you have? Kindly mention their location: ")
    information['Do you have a DR Site in place?'] = input("9) Do you have a DR Site in place? ")

    # "IT details for VA/PT and Configuration Review" section
    information['No of Critical Servers (email, DB, SharePoint etc.)'] = input("10) No of Critical Servers (email, DB, SharePoint etc.): ")
    information['No of Critical Devices (F/w, Switch, Routers, IDS/IPS)'] = input("11) No of Critical Devices (F/w, Switch, Routers, IDS/IPS): ")
    information['No. of Web Applications'] = input("12) No. of Web Applications: ")
    information['No. of Mobile Applications'] = input("13) No. of Mobile Applications: ")
    information['No. of Firewalls'] = input("14) No. of Firewalls: ")
    information['No. of Routers'] = input("15) No. of Routers: ")
    information['No. of Switches'] = input("16) No. of Switches: ")
    information['No. of Desktops/Laptops/Mobile devices used'] = input("17) No. of Desktops/Laptops/Mobile devices used: ")
    information['List all the tools used for IT & Security'] = input("18) List all the tools used for IT & Security: ")

    # Cloud Services and Virtualization
    information['Do you use any Cloud Services? If Yes, List all the services used in cloud infrastructure.'] = input("19) Do you use any Cloud Services? If Yes, List all the services used in cloud infrastructure: ")
    information['Do you use Virtualization? If Yes, List all the services used in Virtualization.'] = input("20) Do you use Virtualization? If Yes, List all the services used in Virtualization: ")

    # Information Security and Data Privacy
    information['Do you already have an Information Security and Data Privacy Program in your Organization? (Yes/ No; If Yes, kindly elaborate)'] = input("21) Do you already have an Information Security and Data Privacy Program in your Organization? (Yes/ No; If Yes, kindly elaborate): ")
    information['Do you have an Information Security Policy in place? Is this Approved and followed in the Organization?'] = input("22) Do you have an Information Security Policy in place? Is this Approved and followed in the Organization?: ")
    information['Do you have an Information Security Officer (ISO)/Chief Information Security Officer (CISO)/ Data Privacy officer (DPO) appointed?'] = input("23) Do you have an Information Security Officer (ISO)/Chief Information Security Officer (CISO)/ Data Privacy officer (DPO) appointed?: ")
    information['Do you have an Information Security Steering Committee in place?'] = input("24) Do you have an Information Security Steering Committee in place?: ")

    # Implementation support
    information['Do you expect implementation support (Asset Inventorization, Classification etc.) for the entire Scope? If yes, please specify the Scope for this-including the number of participating departments and employees in each of these departments.'] = input("25) Do you expect implementation support (Asset Inventorization, Classification etc.) for the entire Scope? If yes, please specify the Scope for this-including the number of participating departments and employees in each of these departments: ")
    information['Do you have to comply with other regulatory requirements? Kindly elaborate.'] = input("26) Do you have to comply with other regulatory requirements? Kindly elaborate: ")
    information['Do you have any other Certifications like, ISO 9001, 14000, etc., Kindly elaborate?'] = input("27) Do you have any other Certifications like, ISO 9001, 14000, etc., Kindly elaborate?: ")

    return information






  def generate_policy(self, business_info, policy):

        prompt = f"""Craft a comprehensive policy document focused on {policy} for this Questionnaire:{business_info}.
                     Make sure to add every element related to the policy. If there is no standard mentioned
                     in the Questionnaire, then you must find what is suitable for the use case from your vast knowledge.
                     Finally, do not forget to map the policy elements to the standard you applied. The document must be tailored to the business, not generic."""

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",
            seed=12345,
            max_tokens=1200,
            messages=[
                {"role": "system", "content": "Act as an expert in information security, legal industry, and cybersecurity, that possess over two decades of experience in managing standard and compliance projects."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']





def main():
    import docx

    info_tool = InformationSecurityTool()

    # Gather information from the user
    gathered_information = info_tool.gather_information()

    # Save gathered information to a text file
    info_tool.save_to_txt(gathered_information, "information_security.txt")

    uae_business_policies = [
    "Data Protection and Privacy ",  # Aligns with UAE’s data protection regulations.
    "Employee Code of Conduct ",  # Standards for employee behavior within the company.
    "Health and Safety ",  # Ensures workplace health and safety compliance.
    "IT and Cybersecurity ",  # Protects company’s information technology assets.
    "Anti-Money Laundering (AML) ",  # Prevents money laundering activities.
    "Human Resources Management ",  # Covers hiring, training, and employee benefits.
    "Environmental ",  # Ensures compliance with UAE environmental laws and regulations.
    "Quality Management ",  # Ensures products and services meet certain standards.
    "Supply Chain and Procurement",  # Governs vendor selection and procurement processes.
    "Customer Data Handling ",  # For handling and protecting customer information.
    "Intellectual Property Rights ",  # Protects the company's and others' intellectual property.
    "Conflict of Interest ",  # Prevents conflicts of interest among employees and management.
    "Social Media ",  # Governs employees' use of social media in relation to the business.
    "Complaints and Grievance ",  # Process for handling customer and employee complaints.
    "Ethics and Compliance ",  # Ensures business operations adhere to legal and ethical standards.
    "Risk Management ",  # Identifies, assesses, and mitigates risks to the business.
    "Business Continuity and Disaster Recovery Plan",  # Plans for continuing operations during and after a disaster.
    "Corporate Social Responsibility (CSR) ",  # Company’s approach to sustainable and ethical operations.
    "Export Control and Sanctions ",  # Ensures compliance with UAE and international trade regulations.
    "Anti-Bribery and Corruption "  # Prevents bribery and corrupt practices in business dealings.
    "Access Control ",  # Guidelines for user access to company resources.
    "Incident Response "  # Procedures for handling security breaches or incidents.
]

    # Define the base directory where you want to save the documents
    base_dir = r"C:\Users\mido2\OneDrive\Desktop\INFOSEC-4TC\infosec\Policies"

    for policy in uae_business_policies:
     generated_policy_text = info_tool.generate_policy(gathered_information, policy)
     file_name = policy.strip().replace(' ', '_') + ".docx"
    
     # Construct the full file path
     full_file_path = os.path.join(base_dir, file_name)
    
     # Create a new document and add the generated text
     doc = docx.Document()
     doc.add_paragraph(generated_policy_text)
    
     # Save the document to the specified path
     doc.save(full_file_path)



if __name__ == "__main__":
    main()