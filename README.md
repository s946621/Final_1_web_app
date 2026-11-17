# RESTful Front-End Web App:

## Project Title - 

**Team Members:**

- 
- 
- 

**Walk-Through Video Link:**
- [Add your video link here]


**Describe your app layout here or paste/link an image of your hand-drawn or digital wireframe:**

- 




## Step-by-Step Checklist & Rubric

# Phase 1: Planning & API Setup [10 pts]
*Set up your mock API and plan your data model.*

- [ ] **Domain & Wireframe:** Choose a unique domain with two related entities (e.g., Clubs & Students). Sketch a wireframe showing all your app pages.
- [ ] **Mock API:** Create an account on mockapi.io and set up two resources with at least 3 sample records each.
- [ ] **API Constants:** Copy your base URL and add these constants to the top of all your `.js` files:
  ```js
  const API_ORIGIN = "https://XXXXXXXX.mockapi.io";
  const API_URL = `${API_ORIGIN}/api/v1`;
  ```

---

# Phase 2: Project Structure [10 pts]
*Build the folder layout.*

- [ ] **Folders & Files:** Create `index.html`, `style.css`, and two subdirectories for your resources. Add 7 HTML files: 4 for the primary resource (list, detail, create, edit) + 3 for the secondary (list, detail, create).
- [ ] **Navigation & Styling:** Every page has a `<nav>` with links between resources and links to `../style.css`.

---

# Phase 3: Display All Records (GET Collection) [15 pts]
*Load and show a list of all primary resource records.*

**Success Criteria:** When you load the list page, you see all records from your API displayed as cards with images, names, and descriptions.

- [ ] **Fetch & Loop:** Write an async function that fetches all records and loops through them to build card HTML.
- [ ] **Render Cards:** Insert cards into a container. Each card shows: image, name, description, and an "Edit" link with the ID in the URL (`?id=3`).
- [ ] **Add New Link:** Include an "Add New [Item]" button linking to the create page.
- [ ] **Click Navigation:** Clicking a card (not Edit) navigates to the detail page with the ID.
- [ ] **Load on Start:** Call the fetch function when the page loads.

---

# Phase 4: Display Single Record (GET by ID) [15 pts]
*Load and show details for one specific record.*

**Success Criteria:** Click a card from the list. See the detail page with the record's info, an Edit button, and related records listed below.

- [ ] **Extract ID:** Get the ID from the query string using `URLSearchParams`.
- [ ] **Fetch & Display:** Fetch the record by ID and display its details on the page.
- [ ] **Show Related Items:** Fetch the other resource type and display records that match (e.g., students linked to a club). Link each to its own detail page.
- [ ] **Edit Link:** Add an "Edit" button linking to the edit page with the ID.

---

# Phase 5: Create New Records (POST) [15 pts]
*Let users add new records via a form.*

**Success Criteria:** Fill out the form, submit, and the new record appears in the list immediately.

- [ ] **Form & Handler:** Create a form with labeled inputs and a submit button. Prevent default submission and read the form values.
- [ ] **POST Request:** Send a POST request to the API with the data as JSON and correct headers.
- [ ] **Default Image:** If image is empty, use a placeholder service.
- [ ] **Redirect:** After success, redirect to the list page. The new record should appear.

---

# Phase 6: Update Records (PUT) [15 pts]
*Let users edit existing records.*

**Success Criteria:** Click Edit, change a field, save, and see the change appear on the detail page and list immediately.

- [ ] **Load & Pre-fill:** Get the ID from the URL, fetch the record, and fill the form with current values.
- [ ] **Form & Handler:** Read the updated values from the form.
- [ ] **PUT Request:** Send a PUT request to the API to save the changes.
- [ ] **Redirect:** After success, redirect to the detail page. Changes should be visible.

---

# Phase 7: Delete Records (DELETE) [10 pts]
*Let users remove records.*

**Success Criteria:** Click Delete, confirm, and the record disappears from the API and list.

- [ ] **Delete Button:** Add a "Delete [Item]" button to the edit page.
- [ ] **DELETE Request:** When clicked, send a DELETE request with a confirmation prompt.
- [ ] **Redirect:** After success, redirect to the list page.

---

# Phase 8: Code Walkthrough Video [10 pts]
*Demonstrate your project with a screen-share recording (5–10 minutes).*

- [ ] **App Demo:** Show the app running. Create, read, edit, and delete a record. Narrate what's happening.
- [ ] **Code Explanation:** Open a fetch function and explain how it works. Show your API endpoint in the browser and explain the JSON (each team member must explain a different fetch function).
- [ ] **Walkthrough:** Explain how your resources relate and how data flows through your app.

---

# Phase 9: Polish & Error Handling [5 pts]
*Make your app more robust.*

- [ ] **Error Handling:** Wrap fetch calls in `try/catch` to handle errors.
- [ ] **User Feedback:** Show a simple success or error message when actions complete.

---

# Bonus Extension Challenges [Extra Credit - 10+ pts each]
*Go beyond the basics. Complete all core phases first, then pick extras.*

- [ ] **Phase 9+: Master Relationships** – On the edit page, let users add/remove related items (e.g., add students to a club via a dropdown). Filter and display them on the detail page.
- [ ] **Third Resource:** Add a third resource type (e.g., "Events" linked to clubs) with create and list pages.
- [ ] **Live Search:** Add a search input to the list page that filters cards as you type.
- [ ] **Sort Options:** Add buttons to sort the list alphabetically or by date created.
- [ ] **Cascading Deletes:** When a record is deleted, automatically remove its ID from all related records' arrays.
- [ ] **Advanced UI:** Add animations, dark mode, or better styling with a CSS framework.

---
