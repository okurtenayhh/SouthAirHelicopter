// South Air Helicopter — shared site behavior

document.addEventListener("DOMContentLoaded", function () {
  var toggle = document.querySelector(".nav-toggle");
  var links = document.querySelector(".nav-links");

  if (toggle && links) {
    toggle.addEventListener("click", function () {
      var isOpen = links.classList.toggle("open");
      toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
    });
  }

  var form = document.querySelector(".contact-form");
  if (form) {
    // Netlify Forms picks the submission up from a POST to the site root.
    // Sending it with fetch keeps the visitor on the page; with JS disabled
    // the form still posts normally and Netlify shows its own thank-you page.
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      var note = form.querySelector(".form-note");
      var button = form.querySelector('button[type="submit"]');
      var showNote = function (text, isError) {
        if (!note) { return; }
        note.textContent = text;
        note.classList.toggle("is-error", isError);
        note.hidden = false;
      };
      if (button) { button.disabled = true; }
      fetch("/", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams(new FormData(form)).toString()
      }).then(function (response) {
        if (!response.ok) { throw new Error(response.status); }
        form.reset();
        showNote("Thanks — your message has been sent. We'll get back to you soon.", false);
      }).catch(function () {
        showNote("Sorry, your message didn't go through. Please call us at 281.648.5187.", true);
      }).then(function () {
        if (button) { button.disabled = false; }
      });
    });
  }

  // Highlight current page in nav based on file name
  var current = window.location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".nav-links a").forEach(function (link) {
    var href = link.getAttribute("href");
    if (href === current) {
      link.classList.add("active");
    }
  });
  // Email addresses copy to the clipboard rather than handing off to a mail
  // client. They remain real mailto: links, so with JS disabled they still
  // work -- and if the copy fails we fall back to opening the client.
  var copyTargets = document.querySelectorAll(".copy-email");
  if (copyTargets.length) {
    var copyStatus = document.createElement("span");
    copyStatus.className = "sr-only";
    copyStatus.setAttribute("role", "status");
    copyStatus.setAttribute("aria-live", "polite");
    document.body.appendChild(copyStatus);

    var writeClipboard = function (text) {
      if (navigator.clipboard && window.isSecureContext) {
        return navigator.clipboard.writeText(text);
      }
      // Fallback for non-secure contexts, e.g. a plain http:// preview.
      return new Promise(function (resolve, reject) {
        var scratch = document.createElement("textarea");
        scratch.value = text;
        scratch.setAttribute("readonly", "");
        scratch.style.position = "fixed";
        scratch.style.top = "-1000px";
        document.body.appendChild(scratch);
        scratch.select();
        var ok = false;
        try { ok = document.execCommand("copy"); } catch (err) { ok = false; }
        document.body.removeChild(scratch);
        if (ok) { resolve(); } else { reject(); }
      });
    };

    copyTargets.forEach(function (link) {
      link.addEventListener("click", function (event) {
        var value = link.getAttribute("data-copy");
        if (!value) { return; }
        event.preventDefault();
        writeClipboard(value).then(
          function () {
            link.classList.add("is-copied");
            copyStatus.textContent = value + " copied to clipboard";
            window.setTimeout(function () {
              link.classList.remove("is-copied");
            }, 1600);
          },
          function () {
            window.location.href = link.getAttribute("href");
          }
        );
      });
    });
  }
});
