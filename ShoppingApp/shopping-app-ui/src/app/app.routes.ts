import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { RegistrationComponent } from './registration/registration.component';
import { LoginComponent } from './login/login.component';

export const routes: Routes = [
  // { path: '', redirectTo: 'auth/login', pathMatch: 'full' },
  { path: 'auth/register', component: RegistrationComponent },
  { path: 'auth/login', component: LoginComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
