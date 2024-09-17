Welcome to the ML_Cybersec wiki!


## Steps to Insert Code in Developer Tools:

**Open Developer Tools:**

Right-click anywhere **on the `webpage` and select `Inspect or press Ctrl+Shift+I (Windows/Linux) or Cmd+Option+I (Mac).`**
**Go to the Console:**

Once the Developer Tools are open, navigate to the Console tab.
**Insert and Run Code:**

You can type or paste JavaScript code into the console and press Enter to run it.

Code: 

```js

alert("Hello, Some code inserted! 👍🏿 ");


```

---

### HTML, CSS, and JavaScript Security

Below is a few steps that can be deployed to enhance web security:

**1. Content Security Policy (CSP)**
Implementing a CSP helps mitigate `Cross-Site Scripting (XSS)` and other injection attacks by controlling what resources the browser can load.

Add this to the `<head>` section:

```html

<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self'; object-src 'none'">

```
This policy allows resources (scripts, styles) only from your domain `('self')` and prevents the loading of untrusted objects and scripts from third-party sources.

**2. XSS Prevention**
To prevent Cross-Site Scripting (XSS), make sure you sanitize and validate all user inputs. If you are going to accept user input in future forms or fields, ensure that you escape or filter any user-generated content before rendering it on the page.

**JavaScript Security Practices:**

Avoid using `innerHTML` for content insertion as it may expose you to XSS attacks. Use `textContent or innerText` instead for plain text insertion.
**Example:**

```js

document.getElementById('msg').textContent = 'Current tasks:';

```
**3. Use HTTPS**
Ensure that your website is served over HTTPS to encrypt communication between your server and the user's browser, preventing man-in-the-middle attacks. If you are not already using it, configure your server to support HTTPS.

**4. Secure Cookies (If Applicable)**
If you're using cookies for session management in the future, ensure they are set with the `HttpOnly, Secure, and SameSite` attributes to prevent them from being accessed via JavaScript or sent in cross-site requests.

**Example:**

```http

Set-Cookie: sessionId=abc123; HttpOnly; Secure; SameSite=Strict;


```
**5. JavaScript Best Practices**
Strict Mode: You already have `'use strict';` in place, which is great. This helps catch common coding mistakes and unsafe actions.
Avoid Inline JavaScript: You're already loading external JavaScript `(app.js)` rather than including inline script tags, which is good security practice. Keep scripts in external files and apply a CSP to restrict the sources.

**6. Refine CSP for External Resources**
If your site ever uses external resources (e.g., Google Fonts, CDN libraries), you can refine the CSP to allow specific sources:

```html

<meta http-equiv="Content-Security-Policy" content="default-src 'self'; font-src https://fonts.googleapis.com; script-src 'self'; style-src 'self' https://fonts.googleapis.com;">

```

**7. Anti-CSRF Tokens (If applicable)**
For forms and any user input that modifies server-side data, implement Cross-Site Request Forgery (CSRF) protection by generating and validating CSRF tokens.




