import { Component} from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-navbar',
  standalone: true,
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss'],
})

export class NavbarComponent  {
  constructor(private router: Router) { }
  
  navigateToHome() {
    this.router.navigate(['/']);
  }

  navigateToLogin() {
    this.router.navigate(['/login']);
  }

  navigateToRegister() {
    this.router.navigate(['/register']);
  }

  navigateToCart() {
    this.router.navigate(['/cart']);
  }

  navigateToProfile() {
    this.router.navigate(['/profile']);
  }

  navigateToLogout() {
    this.router.navigate(['/logout']);
  }

  navigateToAdmin() {
    this.router.navigate(['/admin']);
  }

  navigateToProducts() {
    this.router.navigate(['/products']);
  }

  navigateToUsers() {
    this.router.navigate(['/users']);
  }

  navigateToCategories() {
    this.router.navigate(['/categories']);
  }
}
