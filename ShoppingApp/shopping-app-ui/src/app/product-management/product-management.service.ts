import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

@Injectable({
    providedIn: 'root'
})
export class ProductManagementService {
    private apiUrl = `${environment.apiUrl}/products`;

    constructor(private http: HttpClient) { }

    getAllProducts(): Observable<any> {
        return this.http.get<any>(this.apiUrl, { params: { sessionid: environment.session_id } });
    }

    getProductById(id: number): Observable<any> {
        return this.http.get<any>(`${this.apiUrl}/${id}`, { params: { sessionid: environment.session_id } });
    }

    createProduct(product: any): Observable<any> {
        return this.http.post<any>(`${this.apiUrl}/`, product, { params: { sessionid: environment.session_id } });
    }

    updateProduct(id: number, product: any): Observable<any> {
        return this.http.put<any>(`${this.apiUrl}/${id}`, product, { params: { sessionid: environment.session_id } });
    }

    deleteProduct(id: number): Observable<any> {
        return this.http.delete<any>(`${this.apiUrl}/${id}`, { params: { sessionid: environment.session_id } });
    }
}