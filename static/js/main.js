let clearForm = () => {
  let form = document.getElementById("book-form");
  if (!form) return;
  document.getElementById("non-field-errors")?.remove();
  form
    .querySelectorAll("input:not([name='csrfmiddlewaretoken'])")
    .forEach((input) => {
      input.value = "";
    });
  form.querySelectorAll("select").forEach((select) => {
    select.selectedIndex = 0;
  });
};
