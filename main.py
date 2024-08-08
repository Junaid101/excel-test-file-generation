import pandas as pd

# Create the structure of the Excel project plan based on the provided information

# Define the columns for the task management sheet
columns = [
"Phase", "Task", "Description", "Responsible", "Start Date", "End Date", "Status", "Notes"
]

# Data for the project plan
data = [
# Registration Phase
["Registration", "Complete ITB 2025 Registration", "Ensure registration by the deadline", "Hermes JG", "2024-08-01", "2024-08-30", "Not Started", ""],

# Planning Phase
["Planning", "Define Key Messages", "Agree on key messaging for the event", "Hermes JG, Oleg, Volker", "2024-09-01", "2024-09-30", "Not Started", ""],
["Planning", "Finalize Booth Design", "Work with the agency to finalize the booth design", "Hermes JG", "2024-09-01", "2024-09-30", "Not Started", ""],
["Planning", "Select Giveaways", "Choose and order branded giveaways", "Hermes JG", "2024-09-15", "2024-10-30", "Not Started", ""],

# Pre-Event Communication
["Pre-Event Communication", "Email Marketing Campaign", "Launch email campaigns to drive traffic and appointments", "Hermes JG", "2024-11-01", "2025-02-15", "Not Started", ""],
["Pre-Event Communication", "Social Media Campaign", "Post regular updates and content to social media", "Hermes JG", "2024-11-01", "2025-03-03", "Not Started", ""],
["Pre-Event Communication", "Website Updates", "Create and update ITB 2025 landing page", "Hermes JG", "2024-11-01", "2025-01-15", "Not Started", ""],
["Pre-Event Communication", "Press Release", "Announce participation in ITB 2025", "Hermes JG", "2024-11-01", "2024-11-15", "Not Started", ""],

# Onsite Communication
["Onsite Communication", "Booth Engagement", "Set up interactive digital signage and live demos", "Hermes JG", "2025-02-01", "2025-03-03", "Not Started", ""],
["Onsite Communication", "Social Media Live Updates", "Post real-time content during ITB 2025", "Hermes JG", "2025-03-04", "2025-03-06", "Not Started", ""],
["Onsite Communication", "Networking Events", "Host VIP dinners and private meetings", "Oleg, Volker", "2025-03-04", "2025-03-06", "Not Started", ""],

# Post-Event Communication
["Post-Event Communication", "Lead Follow-Up", "Send thank you emails and follow up with leads", "Hermes JG", "2025-03-07", "2025-03-14", "Not Started", ""],
["Post-Event Communication", "Social Media Wrap-Up", "Post event highlights and customer testimonials", "Hermes JG", "2025-03-07", "2025-03-14", "Not Started", ""],
["Post-Event Communication", "Post-Event Report", "Analyze event success and compile a report", "Hermes JG, Oleg, Volker", "2025-03-10", "2025-03-17", "Not Started", ""]
]

# Convert the data into a DataFrame
df = pd.DataFrame(data, columns=columns)

# Save the DataFrame to an Excel file
file_path = '/mnt/data/HRS_ITB_2025_Project_Plan.xlsx'
df.to_excel(file_path, index=False)

file_path