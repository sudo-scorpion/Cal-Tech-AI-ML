import { Component, OnInit } from '@angular/core';
import { CartService } from './cart.service';
import { ProductManagementService } from '../product-management/product-management.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.scss']
})

export class CartComponent implements OnInit {
  cartItems: any[] = [];
  products: any[] = [];
  newItem: any = {
    items: [
      {
        product_id: 0,
        quantity: 0
      }
    ]
  };
  payment: any = {
    payment_method: 'PayPal',
    payment_details: {
      email: 'dummy@email.com',
    }
  }

  constructor(private cartService: CartService, 
              private productManagementService: ProductManagementService,
              private router: Router ) { }

  ngOnInit(): void {
    this.loadProducts();
    this.loadCartItems();
  }

  getTotal() {
    return this.cartItems.reduce((total, item) => total + (item.product.price * item.quantity), 0);
  }

  loadProducts(): void {
    this.productManagementService.getAllProducts().subscribe(
      data => {
        console.log('Products: ', data);
        this.products = data;
      },
      error => {
        console.error('Error: ', error);
      }
    );
  }

  loadCartItems(): void {
    this.cartService.getCartItems().subscribe(
      data => {
        data.forEach((item: any) => {
          this.cartItems.push({
            ...item,
            product: this.products.find((product: any) => product.id === item.product_id)
          });

          console.log('Cart Items: ', this.cartItems);
          
        });
      },
      error => {
        console.error('Error: ', error);
      }
    );
  }

  addToCart(item: any): void {
    this.cartService.addToCart(item).subscribe(
      data => {
        this.loadCartItems(); // Reload the cart items after adding
      },
      error => {
        console.error('Error: ', error);
      }
    );
  }

  updateCartItem(id: number, item: any): void {
    this.cartService.updateCartItem(id, item).subscribe(
      data => {
        this.cartItems = [];
        this.loadCartItems(); // Reload the cart items after updating
      },
      error => {
        console.error('Error: ', error);
      }
    );
  }

  deleteCartItem(id: number): void {
    this.cartService.deleteCartItem(id).subscribe(
      data => {
        this.cartItems = [];
        this.loadCartItems(); // Reload the cart items after deleting
      },
      error => {
        console.error('Error: ', error);
      }
    );
  }
  checkout() {
    this.cartService.checkout(this.payment).subscribe(
      data => {
        this.cartItems = [];
        this.loadCartItems(); // Reload the cart items after deleting
        alert('Your order is successfully placed');
        // Redirect to the home page
        this.router.navigate(['/']);
      },
      error => {
        console.error('Error: ', error);
      }
    );
  }
}