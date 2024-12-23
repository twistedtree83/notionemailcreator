from notion_client import Client

# Initialize Notion client
notion = Client(auth="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")

# Your Notion database ID
database_id = "7422026afae34537ae2b666505ae1111"

# Function to update Email Link
def update_email_links():
    # Fetch all rows in the database
    response = notion.databases.query(database_id=database_id)
    
    for row in response["results"]:
        page_id = row["id"]  # Get the page ID

        # Extract email from the "Emails" text property
        email_property = row["properties"].get("Emails")
        if not email_property:
            print(f"No 'Emails' property found for page {page_id}")
            continue
        
        # Handle the rich_text type
        if email_property["type"] == "rich_text" and len(email_property["rich_text"]) > 0:
            email = email_property["rich_text"][0]["text"]["content"]
        else:
            print(f"No valid email in 'Emails' property for page {page_id}")
            continue

        # Generate mailto link
        mailto_link = f"mailto:{email}"

        # Update the "Email Link" property
        notion.pages.update(
            page_id=page_id,
            properties={
                "Email Link": {
                    "url": mailto_link
                }
            }
        )
        print(f"Updated email link for {email}")

# Run the function
update_email_links()