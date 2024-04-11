// src/app/registration/registration.service.ts

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})

export class RegistrationService {
  constructor(private http: HttpClient) { }

  registerUser(userData: any) {
    // Send the user registration data to the server as json
    return this.http.post(`${environment.apiUrl}auth/register`, userData);
  }
}