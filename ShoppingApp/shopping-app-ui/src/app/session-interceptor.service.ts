// src/app/session-interceptor.service.ts
import { Injectable } from '@angular/core';
import {
  HttpEvent, HttpInterceptor, HttpHandler, HttpRequest, HttpParams
} from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class SessionInterceptorService implements HttpInterceptor {

  constructor() { }

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    // Retrieve your session ID from where it's stored (e.g., localStorage, service)
    const sessionId = localStorage.getItem('session_id') || environment.session_id;

    // // Clone the request to add the new params
    // const modifiedReq = req.clone({
    // //   params: new HttpParams().set('sessionid', sessionId),
    //   headers: req.headers.set('Authorization', 'Bearer ' + sessionId),
    //   params: req.params.set('sessionid', sessionId)
    // });

    // Clone the request to add the new header
    const modifiedReq = req.clone({
        headers: req.headers.set('Session-ID', sessionId)
    });

    // Pass on the modified request
    return next.handle(modifiedReq);
  }
}
