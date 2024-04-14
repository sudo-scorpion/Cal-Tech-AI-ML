import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})

export class CartService {
  private apiUrl = `${environment.apiUrl}/cart`;

  constructor(private http: HttpClient) { }

  getCartItems(): Observable<any> {
    return this.http.get<any>(this.apiUrl, { params: { sessionid: environment.session_id } });
  }

  addToCart(item: any): Observable<any> {
    console.log("session",  environment.session_id);
    return this.http.post<any>(`${this.apiUrl}/`, item, { params: { sessionid: environment.session_id } });
  }

  updateCartItem(id: number, item: any): Observable<any> {
    return this.http.put<any>(`${this.apiUrl}/${id}`, item, { params: { sessionid: environment.session_id } });
  }

  deleteCartItem(id: number): Observable<any> {
    console.log('Delete Item: ', id);
    confirm('Are you sure you want to delete this item?');
    return this.http.delete<any>(`${this.apiUrl}/${id}`, { params: { sessionid: environment.session_id } });
  }

  checkout(payment: any): Observable<any> {
    console.log('Payment: ', payment);
    return this.http.post<any>(`${environment.apiUrl}/checkout/`, payment, { params: { sessionid: environment.session_id } });
  }
  
}