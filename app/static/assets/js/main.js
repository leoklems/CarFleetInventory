// const navItems = document.querySelectorAll('.nav_item_link, .side_nav_item');

// navItems.forEach((item) => {
//   item.addEventListener('click', (e) => {
//     navItems.forEach((navItem) => navItem.classList.remove('active'));
//     item.classList.add('active');
//   });
// });

// $(document).ready(function() {
//     $('a.nav_item_link').click(function() {
//       $('a.nav_item_link').removeClass('active');
//       $(this).addClass('active');
//     });
//   });

// document.addEventListener('click', (e) => {
//     if (e.target.classList.contains('nav_item_link')) {
//       const navItems = document.querySelectorAll('.nav_item_link');
//       navItems.forEach((navItem) => navItem.classList.remove('active'));
//       e.target.classList.add('active');
//     }


//   });

  // Use htmx to load the form into the popup container
// htmx.on('htmx:load', (e) => {
//     if (e.detail.target.id === 'popup-container') {
//       // Add event listener to close the popup when clicked outside
//       document.addEventListener('click', (e) => {
//         if (e.target !== e.currentTarget && e.target.closest('#popup-container') === null) {
//           htmx.remove(e.detail.target);
//         }
//       });
//     }
//   });

// Listen for htmx:load event
// Store the modal container element in a variable
// let modalContainer = null;

// htmx.on('htmx:load', (e) => {
//   if (e.target.id === 'popup-container') {
//     console.log("MODAL ACTIVATED")
//     modalContainer = e.target; // Store the modal container element

//     // Add event listener to close the modal when clicked outside
//     document.addEventListener('click', (e) => {
//     //   if (e.target !== modalContainer && !modalContainer.contains(e.target)) {
//     //     if (modalContainer) { // Check if the modal container exists
//     //       modalContainer.classList.remove('show-modal'); // Remove the CSS class to hide the modal
//     //       htmx.remove(modalContainer); // Remove the modal container
//     //       modalContainer = null; // Reset the modal container variable
//     //     }
//     //   }

//       if (e.target.id === 'close-modal') {
//         console.log("close activated")
//         if (modalContainer) { // Check if the modal container exists
            
//           modalContainer.classList.remove('show-modal'); // Remove the CSS class to hide the modal
//           htmx.remove(modalContainer); // Remove the modal container
//           modalContainer = null; // Reset the modal container variable
//           console.log("contains passed")
//         }
//       }
//     });

//     // Add CSS class to show the modal
//     modalContainer.classList.add('show-modal');
//   }
// });

  // Get the popup button and container elements
// const popupBtn = document.querySelector('.popup-btn');
// const popupContainer = document.querySelector('.popup-container');

// Add an event listener to the button to toggle the popup container
// popupBtn.addEventListener('click', () => {
//   popupContainer.style.display = 'block';
// });

// Add an event listener to the popup container to close it when clicked outside
// popupContainer.addEventListener('click', (e) => {
//   if (e.target === popupContainer) {
//     popupContainer.style.display = 'none';
//   }
// });

// function showFormInModal(){
//     var formHtml = document.getElementById('popup-container').innerHTML;
//     console.log("form created")
//     swal({
//         title:"Form",
//         html:formHtml,
//         showCloseButton: true,
//     });
// }

// function showFormInModal() {
//     const popupContainer = document.getElementById('popup-container');
//     popupContainer.classList.add('show-modal');
//     document.addEventListener('click', (e) => {
//         if (e.target !== popupContainer && e.target.closest('#popup-container') === null) {
//             popupContainer.classList.remove('show-modal');
//         }
//     });
// }
  
    // Check the current route and add the active class to the corresponding link
    function checkRoute() {
      let links = document.querySelectorAll('a[hx-get]');
      const currentUrl = window.location.pathname;
      links.forEach((link) => {
        const href = link.getAttribute('href');
        if (currentUrl === "/" && href ==="/ ") {
          link.classList.add('active');
        } else 
        if (href && currentUrl.includes(href)) {
            link.classList.add('active');
        } else {
            // console.log("failed")
          link.style.color = ''; // Reset the color
        }
      });
    }
  
    // Call the checkRoute function on page load and after each hx:afterSwap event
    document.addEventListener('DOMContentLoaded', checkRoute);
    document.addEventListener('htmx:afterSwap', checkRoute);
function menueToggle() {
  document.getElementById('side_nav').classList.toggle("show_grid")
}

// Store the modal container element in a variable
let modalContainer = null;
let closeModal = false; // Store the modal container element
let sideNav = document.getElementById('side_nav');
let sideNavClass = document.getElementsByClassName('side_nav');
let menuCloseButton = document.getElementById('menu-close');

// Add event listener to close the modal when clicked outside
document.addEventListener('click', (e) => {
  if (modalContainer && e.target !== modalContainer && !modalContainer.contains(e.target)) {
    if (modalContainer) { // Check if the modal container exists
      modalContainer.classList.remove('show-modal'); // Remove the CSS class to hide the modal
    //   htmx.remove(modalContainer); // Remove the modal container
      // modalContainer.innerHTML = 'Open'; // Clear the modal container content
      modalContainer = null; // Reset the modal container variable
    }
  }

  if (e.target.id === 'menu-show') {
    // console.log(document.getElementById('side_nav'))
    document.getElementById('side_nav').classList.toggle("show_grid")
    // if (sideNav.style.display === "none") {
    //   sideNav.style.display = "grid"
    // } else {
    //   sideNav.style.display = "none"
    // }
  }

  if (e.target.id === 'menu-close') {
    // console.log(document.getElementById('side_nav'))
    document.getElementById('side_nav').classList.toggle("show_grid")
  }

  if (e.target.id === 'close-modal') {
    if (modalContainer) { // Check if the modal container exists
      modalContainer.classList.remove('show-modal'); // Remove the CSS class to hide the modal
      // htmx.remove(modalContainer); // Remove the modal container
      // modalContainer.innerHTML = 'Open'; // Clear the modal container content
      modalContainer = null; // Reset the modal container variable
      closeModal = true;
    }
  }
});

htmx.on('htmx:load', (e) => {
  if (e.target.id === 'add-staff-container') {
    modalContainer = e.target; // Store the modal container element
    e.target.classList.add('show-modal'); // Add CSS class to show the modal
  }

  if (e.target.id === 'checkin-staff-container') {
    modalContainer = e.target; // Store the modal container element
    e.target.classList.add('show-modal'); // Add CSS class to show the modal
  }

  if (e.target.id === 'add-project-container') {
    modalContainer = e.target; // Store the modal container element
    e.target.classList.add('show-modal'); // Add CSS class to show the modal
  }

  if (e.target.id === 'project-detail-container') {
    modalContainer = e.target; // Store the modal container element
    e.target.classList.add('show-modal'); // Add CSS class to show the modal
  }

  if (e.target.id === 'add-task-container') {
    modalContainer = e.target; // Store the modal container element
    e.target.classList.add('show-modal'); // Add CSS class to show the modal
  }

  if (e.target.id === 'add-finance-container') {
    modalContainer = e.target; // Store the modal container element
    e.target.classList.add('show-modal'); // Add CSS class to show the modal
  }

  if (e.target.id === 'edit-stuff-container') {
    modalContainer = e.target; // Store the modal container element
    e.target.classList.add('show-modal'); // Add CSS class to show the modal
  }
});
console.log("loaded page")
document.addEventListener('load', function() {
  
  let button = document.getElementById('add-staff');

  button.addEventListener('click', (e) => {
    let targetId = document.getElementById('add-staff-container');
    targetId.classList.add('show-modal');

  });
});
