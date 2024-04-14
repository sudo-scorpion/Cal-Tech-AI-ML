import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

@Injectable({
    providedIn: 'root'
})
export class CategoryManagementService {
    // Define your API endpoint prefix here and get api url from environment.ts

    private baseUrl = `${environment.apiUrl}/categories`;

    constructor(private http: HttpClient) { }

    getAllCategories(): Observable<any> {
        return this.http.get(`${this.baseUrl}`, { params: { sessionid: environment.session_id } });
    }

    getCategoryById(categoryId: number): Observable<any> {
        return this.http.get(`${this.baseUrl}/${categoryId}`, { params: { sessionid: environment.session_id } });
    }

    createCategory(category: any): Observable<any> {
        return this.http.post(`${this.baseUrl}/`, category, { params: { sessionid: environment.session_id } });
    }

    updateCategory(categoryId: number, category: any): Observable<any> {
        return this.http.put(`${this.baseUrl}/${categoryId}`, category.name, { params: { sessionid: environment.session_id } });
    }

    deleteCategory(categoryId: number): Observable<any> {
        return this.http.delete(`${this.baseUrl}/${categoryId}`, { params: { sessionid: environment.session_id } });
    }
}