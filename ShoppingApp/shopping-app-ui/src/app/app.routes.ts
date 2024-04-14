import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { RegistrationComponent } from './registration/registration.component';
import { LoginComponent } from './login/login.component';
import { CategoryManagementComponent } from './category-management/category-management.component';
import { ProductManagementComponent } from './product-management/product-management.component';
import { CartComponent } from './cart/cart.component';

export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'register', component: RegistrationComponent },
  { path: 'login', component: LoginComponent },
  { path: 'categories', component: CategoryManagementComponent },
  { path: 'products', component: ProductManagementComponent },
  { path: 'cart', component: CartComponent },
  { path: '**', redirectTo: '' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
