import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms'; 
import { ReactiveFormsModule } from '@angular/forms';
import { RegistrationComponent } from './registration/registration.component';
import { LoginComponent } from './login/login.component';

 
@NgModule({
  imports: [
    FormsModule,
    ReactiveFormsModule
  ], 
  declarations: [
    RegistrationComponent,
    LoginComponent,
  ],
  }
)

export class AppModule { }