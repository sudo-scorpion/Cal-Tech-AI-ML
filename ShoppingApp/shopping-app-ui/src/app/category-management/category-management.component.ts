import { Component, OnInit } from '@angular/core';
import { CategoryManagementService } from './category-management.service';

@Component({
  selector: 'app-category-management',
  templateUrl: './category-management.component.html',
  styleUrls: ['./category-management.component.scss'],
})

export class CategoryManagementComponent implements OnInit {
  newCategory: any = {
    name: ''
  };
  categories: any[] = [];

  constructor(private categoryService: CategoryManagementService) { }

  ngOnInit(): void {
    this.getAllCategories();
  }

  getAllCategories(): void {
    this.categoryService.getAllCategories().subscribe(
      data => {
        this.categories = data;
      },
      error => {
        console.error('Error:', error);
      }
    );
  }

  createCategory(category: any): void {
    this.categoryService.createCategory(category).subscribe(
      data => {
        this.getAllCategories(); // Refresh the list after creation
        this.newCategory = { name: '' }; // Clear the form after creation
      },
      error => {
        console.error('Error:', error);
      }
    );
  }

  updateCategory(categoryId: number, category: any): void {
    this.categoryService.updateCategory(categoryId, category).subscribe(
      data => {
        this.getAllCategories(); // Refresh the list after update
      },
      error => {
        console.error('Error:', error);
      }
    );
  }

  deleteCategory(categoryId: number): void {
    this.categoryService.deleteCategory(categoryId).subscribe(
      data => {
        this.getAllCategories(); // Refresh the list after deletion
      },
      error => {
        console.error('Error:', error);
      }
    );
  }
}