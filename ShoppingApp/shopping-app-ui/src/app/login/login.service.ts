import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  constructor(private http: HttpClient) { }

  login(credentials: any): Observable<any> {
    // Assuming the backend endpoint for login is '/auth/login'
    return this.http.post(`${environment.apiUrl}auth/login`, credentials);
  }
}
