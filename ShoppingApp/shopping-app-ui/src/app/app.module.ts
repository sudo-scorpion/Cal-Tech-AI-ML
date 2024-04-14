import { BrowserModule } from '@angular/platform-browser'; // or import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms'; 
import { ReactiveFormsModule } from '@angular/forms';
import { HomeComponent } from './home/home.component';
import { RegistrationComponent } from './registration/registration.component';
import { LoginComponent } from './login/login.component';
import { CategoryManagementComponent } from './category-management/category-management.component';
import { ProductManagementComponent } from './product-management/product-management.component';
import { CartComponent } from './cart/cart.component';
import { SessionInterceptorService } from './session-interceptor.service';
import { HTTP_INTERCEPTORS } from '@angular/common/http';

 
@NgModule({
  imports: [
    BrowserModule, // or CommonModule
    FormsModule,
    ReactiveFormsModule,
  ], 
  declarations: [
    HomeComponent,
    RegistrationComponent,
    LoginComponent,
    CategoryManagementComponent,
    ProductManagementComponent,
    CartComponent,
  ],
  providers: [
    {
      provide: HTTP_INTERCEPTORS,
      useClass: SessionInterceptorService,
      multi: true
    }
  ],
  }
)

export class AppModule { }