import { Component } from '@angular/core';
import { LoginService } from './login.service';
import { environment } from '../../environments/environment';
import { Router } from '@angular/router';

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

  constructor(private loginService: LoginService, private router: Router) { }

  onSubmit() {
    console.log('User data:', this.userData);
    this.loginService.login(this.userData).subscribe(
      response => {
        // Store the session ID in the environment
        environment.session_id = response.session_id;
        console.log('User logged in successfully!', response);
        alert('User logged in successfully!');
        // Clear the form
        this.userData = {
          username: '',
          password: ''
        };
        // Redirect the user to the home page
        this.router.navigate(['/']);
      },
      error => {
        console.error('Failed to login user!', error);
        alert('Failed to login user!');
      }
    );
  }
}
