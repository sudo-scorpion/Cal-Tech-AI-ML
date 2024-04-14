import { Component, OnInit } from '@angular/core';
import { ProductManagementService } from '../product-management/product-management.service';
import { CategoryManagementService } from '../category-management/category-management.service';
import { CartService } from '../cart/cart.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  title = 'PopCart - Home Page';
  products: any[] = [];
  categories: any[] = [];
  selectedCategory: any = null;

  constructor(
    private productService: ProductManagementService,
    private categoryService: CategoryManagementService,
    private cartService: CartService
  ) {};

  ngOnInit() {
    console.log('Home Component Initialized');
    this.loadCategories();
  }

  loadCategories(): void {
    this.categoryService.getAllCategories().subscribe(
      data => {
        this.categories = data;
        this.selectedCategory = this.categories[0];
        this.loadProducts();
      },
      error => {
        console.error('Error: ', error);
      }
    );
  }

  loadProducts(): void {
    this.productService.getAllProducts().subscribe(
      data => {
        if (this.selectedCategory && typeof this.selectedCategory !== 'object') {
          this.products = [];
          data.forEach((product: any) => {
            if (parseInt(product.category_id) === parseInt(this.selectedCategory)) {
              this.products.push(product);
            }
          });
        }
        else {
          this.products = data;
        }
      },
      error => {
        console.error('Error: ', error);
      }
    );
  }

  addToCart(productId: number): void {
    const newItem = {
      items: [
        {
          product_id: productId,
          quantity: 1
        }
      ]
    };

    this.cartService.addToCart(newItem).subscribe(
      data => {
        console.log('Item added to cart');
      },
      error => {
        console.error('Error: ', error);
      }
    );
  }
}