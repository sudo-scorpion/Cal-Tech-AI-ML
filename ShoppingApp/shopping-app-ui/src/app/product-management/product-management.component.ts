import { Component, OnInit } from '@angular/core';
import { ProductManagementService } from './product-management.service';
import { CategoryManagementService } from '../category-management/category-management.service';

@Component({
  selector: 'app-product-management',
  templateUrl: './product-management.component.html',
  styleUrls: ['./product-management.component.scss'],
})

export class ProductManagementComponent implements OnInit {
  products: any[] = [];
  categories: any[] = [];
  newProduct: any = { name: '', price: 0, category_id: 0 };

  constructor(
    private productService: ProductManagementService,
    private categoryService: CategoryManagementService
  ) {}

  ngOnInit(): void {
    this.loadProducts();
    this.loadCategories();
  }

  loadProducts(): void {
    this.productService.getAllProducts().subscribe(
      data => { this.products = data; },
      error => { console.error('Error: ', error); }
    );
  }

  loadCategories(): void {
    this.categoryService.getAllCategories().subscribe(
      data => { this.categories = data; },
      error => { console.error('Error: ', error); }
    );
  }

  createProduct(product: any): void {
    this.productService.createProduct(product).subscribe(
      data => { this.loadProducts(); },
      error => { console.error('Error: ', error); }
    );
  }

  updateProduct(id: number, product: any): void {
    this.productService.updateProduct(id, product).subscribe(
      data => { this.loadProducts(); },
      error => { console.error('Error: ', error); }
    );
  }

  deleteProduct(id: number): void {
    this.productService.deleteProduct(id).subscribe(
      data => { this.loadProducts(); },
      error => { console.error('Error: ', error); }
    );
  }
}
