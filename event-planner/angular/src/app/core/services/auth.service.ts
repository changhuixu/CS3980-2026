import { HttpClient } from '@angular/common/http';
import { inject, Injectable, signal } from '@angular/core';
import { Router } from '@angular/router';
import { map } from 'rxjs';
import { auth_url } from '../../api-urls';
import { AppUser } from '../models/app-user';

@Injectable({ providedIn: 'root' })
export class AuthService {
  private readonly apiUrl = auth_url;
  private router = inject(Router);
  private http = inject(HttpClient);
  private _user = signal<AppUser>(this.getUserFromStorage());
  user = this._user.asReadonly();

  getUserFromStorage(): AppUser {
    const u = localStorage.getItem('user');
    if (!u) {
      return {
        username: '',
        role: '',
        token: '',
        expiry: new Date(),
      };
    }
    return JSON.parse(u);
  }

  signup(username: string, password: string) {
    return this.http.post(`${this.apiUrl}/signup`, {
      email: username,
      password,
    });
  }

  login(username: string, password: string) {
    let formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);
    return this.http.post<AppUser>(`${this.apiUrl}/sign-in`, formData).pipe(
      map((x) => {
        localStorage.setItem(
          'user',
          JSON.stringify({
            username: username,
            role: x.role,
            token: x.token,
            expiry: x.expiry,
          }),
        );
        this._user.set(this.getUserFromStorage());
        return x;
      }),
    );
  }

  logout() {
    localStorage.removeItem('user');
    this._user.set(this.getUserFromStorage());
    this.router.navigateByUrl('/login');
  }
}
