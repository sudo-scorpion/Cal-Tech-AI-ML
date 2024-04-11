import { Component } from '@angular/core';
import { RegistrationService } from './registration.service';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.scss'],
  providers: [RegistrationService]
})

export class RegistrationComponent {
  userData = {
    username: '',
    email: '',
    password: ''
  };

  constructor(private registrationService: RegistrationService) { }

  onSubmit() {
    console.log('User data:', this.userData);
    this.registrationService.registerUser(this.userData).subscribe(
      response => {
        console.log('User registered successfully!', response);
        // Clear the form
        this.userData = {
          username: '',
          email: '',
          password: ''
        };
        // Redirect the user to the login page
        window.location.href = '/auth/login';
      },
      error => {
        console.error('Failed to register user!', error);
      }
    );
  }
}
