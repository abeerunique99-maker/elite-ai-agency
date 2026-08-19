# Onboarding Automation Plan for doly

Here's a structured 3-step client onboarding automation plan for Doly, focusing on welcome, asset collection, and project management setup.

**Core Automation Tools Recommended:**

*   **CRM (Client Relationship Management):** HubSpot, Salesforce, Pipedrive (to trigger workflows, manage client status)
*   **Email Marketing/Automation Platform:** ActiveCampaign, Mailchimp, ConvertKit (for personalized email sequences)
*   **Project Management Tool:** Asana, ClickUp, Trello, Monday.com (for internal task management, client portal if applicable)
*   **Online Forms/Surveys:** Typeform, Google Forms, Jotform (for structured data/asset collection)
*   **Scheduling Tool:** Calendly, Acuity Scheduling (for booking kick-off calls)
*   **Cloud Storage:** Google Drive, Dropbox, SharePoint (for asset organization)

---

## Client Onboarding Automation Plan: Doly

**Goal:** To provide Doly with a seamless, professional, and efficient onboarding experience, gathering all necessary information and setting up the project for success with minimal manual effort.

---

### Step 1: The Warm Welcome & Initial Orientation

**Trigger:** Contract Signed / First Payment Received (automatically updated in CRM).

**Automation Focus:** Establishing a positive first impression, confirming the partnership, and setting expectations for the immediate next steps.

---

**1.1 Internal Notification & CRM Update**

*   **Automation:** CRM automatically changes Doly's status to "Onboarding" and assigns the Project Manager (PM) or Account Manager.
*   **Action:** CRM sends an internal notification (email/Slack) to the sales team, PM, and relevant stakeholders (e.g., lead designer, developer) about the new client, Doly.
*   **Output:** Team is aware of Doly's onboarding, project lead is assigned.

---

**1.2 Welcome Email Sequence (Automated)**

*   **Automation Tool:** Email Marketing Platform, triggered by CRM status change.

    *   **Email 1 (Immediately after trigger): "Welcome Aboard, Doly! Let's Get Started on Your Project!"**
        *   **Sender:** Your dedicated Account Manager or PM.
        *   **Subject:** Welcome to [Your Company Name], Doly! Let's build something great!
        *   **Content:**
            *   Personalized greeting to Doly.
            *   Excitement about the partnership.
            *   Brief overview of what to expect in the onboarding process (e.g., "We'll be collecting some info, setting up our tools, and then scheduling a kick-off call.").
            *   Introduce their primary point of contact (PM/AM) with photo and contact details.
            *   Link to a basic "Welcome Kit" or "Client Portal" page on your website (if applicable), which might include FAQs, team bios, or testimonials.
            *   Reiterate key value proposition.
            *   **Call to Action:** "Keep an eye out for our next email, which will guide you through providing the initial information we need."
        *   **Attachment (Optional):** A simple "What to Expect" one-pager or project roadmap.

    *   **Email 2 (24 hours after Email 1, if no action from Doly on future steps): "Quick Check-in: Getting Ready for Your Project, Doly!"**
        *   **Subject:** Just checking in, Doly! Your project is waiting!
        *   **Content:** A friendly reminder that you're excited to start and the next steps are coming soon. Reiterate the value.

---

### Step 2: Asset & Information Collection

**Trigger:** 2-4 hours after Email 1 is sent (or upon Doly opening Email 1).

**Automation Focus:** Systematically gathering all necessary assets, access credentials, and critical information from Doly required to commence the project.

---

**2.1 Client Onboarding Form & Asset Portal**

*   **Automation Tool:** Online Forms (e.g., Typeform, Jotform) integrated with Cloud Storage (Google Drive) and Project Management Tool.

    *   **Email 3 (Automated): "Time to Share! Your Project Information & Asset Request, Doly."**
        *   **Sender:** Your dedicated Account Manager or PM.
        *   **Subject:** Doly, let's gather what we need for a smooth project start!
        *   **Content:**
            *   Thank Doly for their enthusiasm.
            *   Clearly explain *why* this information is needed (e.g., "to ensure we align with your brand, get necessary access, and understand your preferences fully").
            *   **Primary Call to Action:** A prominent link to your dedicated online onboarding form/portal.
            *   **List of Required Items:** Clearly list what's needed (e.g., brand guidelines, logos, website access, social media logins, content drafts, target audience insights, competitor analysis).
            *   **Instructions:** How to submit files (upload directly to form, shared cloud folder link).
            *   **Deadline:** A soft internal deadline for submitting assets.
            *   **Offer Help:** Reiterate that their PM is available for assistance.

*   **Onboarding Form/Portal Contents:**
    *   **Basic Project Info Confirmation:** Reconfirm project scope, primary goals.
    *   **Brand Assets:** Upload fields for logos (various formats), brand guidelines, fonts, imagery.
    *   **Access Credentials:** Secure fields for website backend access, hosting details, social media logins, analytics access (use a secure method like LastPass enterprise or a dedicated credential manager if not submitting directly through the form).
    *   **Content:** Fields for existing content, links to relevant pages, content strategy documents.
    *   **Competitor Analysis/Inspiration:** Fields for links to competitors, desired aesthetics/functionality.
    *   **Key Stakeholders:** Names, roles, and contact info for other decision-makers.

---

**2.2 Automated Reminders & Internal Progress Tracking**

*   **Automation Tool:** Email Marketing Platform (triggered by form completion status) & Project Management Tool.
    *   **Email 4 (Automated): "Just a Nudge: Your Project Assets Are Waiting, Doly!"**
        *   **Trigger:** If onboarding form is not completed within 2-3 days of Email 3 being sent.
        *   **Content:** Friendly reminder, re-emphasize the importance of the assets, link to the form again.
    *   **Internal Task (PM Tool):** When the form is submitted, a task "Review Doly's Submitted Assets" is automatically created for the PM.
    *   **Cloud Storage Automation:** Form submissions automatically deposit files into a dedicated Google Drive/Dropbox folder for Doly, with pre-set subfolders (e.g., "Assets," "Content," "Access").

---

### Step 3: Project Management Setup & Kick-off Readiness

**Trigger:** Doly completes the onboarding form and assets are submitted (marked "received" by PM in CRM/PM Tool).

**Automation Focus:** Setting up internal project environments, inviting Doly to relevant platforms, and scheduling the official kick-off meeting.

---

**3.1 Internal Project Setup & Team Briefing**

*   **Automation Tool:** Project Management Tool (e.g., Asana, ClickUp), integrated with CRM.
*   **Action:**
    *   **Project Creation:** CRM automatically creates a new project in the PM tool for "Doly - [Project Name]" using a pre-defined project template.
        *   This template includes standard phases, tasks, subtasks, and internal deadlines.
    *   **Team Assignment:** Key team members (e.g., designer, copywriter, developer) are automatically assigned to relevant sections/tasks within the PM tool.
    *   **Information Transfer:** Data from Doly's onboarding form is automatically populated into relevant custom fields or initial tasks within the PM tool.
    *   **Internal Kick-off Task:** A task "Internal Team Briefing for Doly" is created for the PM and relevant team members.

---

**3.2 Client Access & Kick-off Scheduling**

*   **Automation Tool:** Email Marketing Platform, Scheduling Tool (Calendly), Project Management Tool.

    *   **Email 5 (Automated): "Great News, Doly! Your Project is Taking Shape & It's Time to Kick-off!"**
        *   **Sender:** Your dedicated Account Manager or PM.
        *   **Subject:** Doly, your project portal is ready! Let's schedule our Kick-off!
        *   **Content:**
            *   Thank Doly for providing all the necessary information.
            *   Inform them that the team is now reviewing everything and preparing.
            *   **Call to Action 1 (Scheduling):** Provide a direct link to your Calendly/Acuity Scheduling page for the "Project Kick-off Meeting."
                *   *Tip:* Set the scheduling tool to automatically block out the PM's calendar and create a Zoom/Google Meet link.
            *   **Call to Action 2 (Client Portal Access - Optional):** If you provide Doly with access to your PM tool (e.g., Asana guest access):
                *   "We've also set up your dedicated client portal in [PM Tool Name]. You'll receive a separate invitation shortly, but here's a link to log in: [PM Tool Link]."
                *   Briefly explain what they can expect to see/do in the portal (e.g., track progress, share feedback).
            *   **Kick-off Meeting Agenda:** Briefly outline what will be discussed during the kick-off meeting.
            *   Reiterate excitement and readiness.

---

**3.3 Final Internal Review & Kick-off Prep**

*   **Automation Tool:** Project Management Tool.
*   **Action:**
    *   **Task Creation:** A task "Prepare for Doly's Kick-off Meeting" is automatically assigned to the PM with a due date prior to the scheduled call. This task includes subtasks like "Review assets," "Draft kick-off agenda," "Confirm team availability."
    *   **Meeting Confirmation:** Calendly automatically sends meeting confirmations and reminders to both Doly and your internal team.

---

By following this automated 3-step plan, you ensure Doly feels valued, all critical information is efficiently collected, and your internal team is fully prepared for a successful project launch. This reduces manual errors, saves time, and significantly improves the client experience.