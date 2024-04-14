import { Component } from '@angular/core';
import { RegistrationService } from './registration.service';
import { Router } from '@angular/router';
import { warn } from 'console';

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
    password: '',
    role: 'user',
    admin_token: ''
  };

  isAdmin = false;

constructor(private registrationService: RegistrationService, private router: Router) { }

  onSubmit() {
    if (this.userData.role === 'admin' && !this.userData.admin_token) {
      alert('Admin token is required for admin registration');
      return;
    }

    if (this.isAdmin) {
      this.registrationService.registerAdmin(this.userData).subscribe(
        response => {
          console.log('Registration successful', response);
          alert('Registration successful');
          // Navigate to another page here if needed
          this.router.navigate(['/login']);
        },
        error => {
          console.log('Registration failed', error);
          alert('Registration failed');
        }
      );
    } else {
      this.registrationService.registerUser(this.userData).subscribe(
        response => {
          console.log('Registration successful', response);
          alert('Registration successful');
          // Navigate to another page here if needed
          this.router.navigate(['/login']);
        },
        error => {
          console.log('Registration failed', error);
          alert('Registration failed');
        }
      );
    }
  }

  onRoleChange(event: Event): void {
    const selectElement = event.target as HTMLSelectElement; // Safely cast to the specific element type
    const role = selectElement.value;
    console.log('Role changed to:', role);
    // Add any additional logic if necessary when role changes
  }
  
}