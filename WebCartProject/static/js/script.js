
// Static data for tech products since I will need the database to load the data
const techProducts = [
    {
        name: 'Laptop',
        description: 'Powerful laptop for all your computing needs.',
        price: 999.99,
        imageURL: 'https://images.pexels.com/photos/205421/pexels-photo-205421.jpeg?cs=srgb&dl=pexels-craig-dennis-205421.jpg&fm=jpg'
    },
    {
        name: 'Smartphone',
        description: 'Latest smartphone with advanced features.',
        price: 499.99,
        imageURL: 'smartphone.jpg'
    },
    {
        name: 'Headphones',
        description: 'High-quality headphones for immersive audio.',
        price: 129.99,
        imageURL: 'headphones.jpg'
    },
    {
        name: 'Poop',
        description: 'poop',
        price: 1.00,
        imageURL: 'poop.jpg'
    },
    {
        name:'Nose Ring',
        description: 'Its a small nose ring',
        price: 10.00,
        imageURL: 'nosering.jpg',
    },
    {
        name:'Nose Ring',
        description: 'Its a small nose ring',
        price: 10.00,
        imageURL: 'nosering.jpg',
    },
    {
        name:'Nose Ring',
        description: 'Its a small nose ring',
        price: 10.00,
        imageURL: 'nosering.jpg',
    },
    {
        name:'Nose Ring',
        description: 'Its a small nose ring',
        price: 10.00,
        imageURL: 'nosering.jpg',
    },
    {
        name:'Nose Ring',
        description: 'Its a small nose ring',
        price: 10.00,
        imageURL: 'nosering.jpg',
    },
    {
        name:'Nose Ring',
        description: 'Its a small nose ring',
        price: 10.00,
        imageURL: 'nosering.jpg',
    }
    
];

// Function to display tech products
function displayTechProducts() {
    // Loop through each tech product in the static data
    techProducts.forEach(function(product) {
        // Display tech product information
        $('#productList').append(`
            <div class="product">
                <img src="${product.imageURL}" alt="${product.name}">
                <h3>${product.name}</h3>
                <p>${product.description}</p>
                <p>Price: $${product.price}</p>
                <button>Add to Cart</button>
            </div>
        `);
    });
    
$(".product").on("click",function(){
    alert("You suck");
})
}



//This is the function when I have the database
// function displayTechProducts() {
//     //You will have to use ajax to fetch the get_products in the db
//     $.ajax({
//         url: '/get_products',
//         method: 'GET',
//         success: function(data){
//             data.forEach(function(product){
//                 $('#productList').append(`
//                     <div class="product">
//                     <img src="${product.imageURL}" alt="${product.name}">
//                     <h3>${product.name}</h3>
//                     <p>${product.description}</p>
//                     <p>Price: $${product.price}</p>
//                     <button>Add to Cart</button>
//                     </div>
//                     `);
//             });
//         },
//         error: function(error) {
//             console.log(error);
//         }
//     });
// }

// Call the function to display tech products when the page loads
$(document).ready(function() {
    displayTechProducts();
});
