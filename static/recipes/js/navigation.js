function showMenu() {
    const nav = document.getElementById("nav")
    nav.classList.toggle("hide");
    nav.classList.toggle("nav-show");
  }
  
  function dismiss() {
    const message = document.getElementById("message")
    message.classList.toggle("hide");
  }
  
  function updateDialog() {
    const update = document.getElementById('update_card')
    update.classList.toggle("hide");
    update.classList.toggle("update_card");
  }
  
  function deleteDialog() {
    const delete_recipe = document.getElementById('delete_card')
    delete_recipe.classList.toggle("hide");
    delete_recipe.classList.toggle("delete_card");
  }
  
  function closeUpdate() {
    const update = document.getElementById('update_card')
    if (update.classList.contains('update_card')) {
      update.classList.toggle("update_card");
      update.classList.toggle("hide");
    }
  }
  
  function closeDelete() {
    const delete_recipe = document.getElementById('delete_card')
    if (delete_recipe.classList.contains('delete_card')) {
      delete_recipe.classList.toggle("hide");
      delete_recipe.classList.toggle("delete_card");
    }
  }
  
  function closeDialog() {
    closeDelete()
    closeUpdate()
  }