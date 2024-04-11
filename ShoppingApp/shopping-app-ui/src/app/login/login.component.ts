import { Component } from '@angular/core';
import { LoginService } from './login.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
  providers: [LoginService]
})

export class LoginComponent {
  userData = {
    username: '',
    password: ''
  };

  constructor(private loginService: LoginService) { }

  onSubmit() {
    console.log('User data:', this.userData);
    this.loginService.login(this.userData).subscribe(
      response => {
        console.log('User logged in successfully!', response);
        // Clear the form
        this.userData = {
          username: '',
          password: ''
        };
        // Redirect the user to the home page
        window.location.href = '/';
      },
      error => {
        console.error('Failed to login user!', error);
      }
    );
  }
}
