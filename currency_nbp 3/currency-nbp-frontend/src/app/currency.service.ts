import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CurrencyService {
  private apiUrl = 'http://localhost:8000/api/';

  constructor(private http: HttpClient) { }

  getRates(): Observable<any> {
    return this.http.get<any>(this.apiUrl + 'get-rates/');
  }
}