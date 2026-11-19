const API_ORIGIN = "https://6afcaf10892984c4494bdfaf.mockapi.io";
const API_URL = `${API_ORIGIN}/targot`;

let all_products = [];

async function fetchProducts() {
  const response = await fetch(`${API_URL}/Product`);
  all_products = await response.json();
  console.log(all_products);
  for(let product of all_products){
      document.getElementById('products').innerHTML +=
    //   Card populated by API data
      `<div class='product_card' data-id='${product['id']}'>
        <img src='${product['thumbnail']}' alt='${product['name']}'>
        <h3>${product['name']}</h3>
        <p>${product['price']}$</p>
        <p>There are ${product['stock']}</p>
      </div>`
  }

  // The add card always goes last
//   document.getElementById('clubs').innerHTML +=
//     `<a href='new_club.html' class='club_card add_card' aria-label='Create a new club'>
//       <span class='plus'>+</span>
//       <span class='add_label'>Add a new club</span>
//     </a>`
}

// Clicking a card opens its club page; the Edit button keeps its own link
// document.getElementById('products').addEventListener('click', (event) => {
//   const card = event.target.closest('.club_card[data-id]');
//   if (!card || event.target.closest('.card_edit_button')) return;
//   window.location.href = `club.html?id=${card.dataset.id}`;
// });

window.addEventListener("load", fetchProducts);