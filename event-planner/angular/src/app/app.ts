import { Component, inject } from '@angular/core';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';
import { AuthService } from './core';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, RouterLink, RouterLinkActive],
  template: `
    <header>
      <nav class="navbar navbar-expand-md navbar-dark bg-dark px-3">
        <a class="navbar-brand" routerLink="">Event Planner</a>
        <div class="collapse navbar-collapse">
          <ul class="navbar-nav me-auto">
            <li class="nav-item">
              <a class="nav-link" routerLink="events" routerLinkActive="active">Events</a>
            </li>
            @if (user().role === 'SuperAdmin') {
              <li class="nav-item">
                <a class="nav-link" routerLink="admin" routerLinkActive="active">Admin</a>
              </li>
            }
          </ul>
          <div class="form-inline">
            @if (user().username) {
              <span class="text-warning me-2">{{ user().username }}</span>
              <button class="btn btn-outline-success my-2 my-sm-0" type="button" (click)="logout()">
                Logout
              </button>
            }
          </div>
        </div>
      </nav>
    </header>
    <main class="container d-flex flex-column flex-grow-1 h-100 w-100">
      <router-outlet></router-outlet>
    </main>
  `,
  styles: [
    `
      .active {
        font-weight: bold;
        color: #fff03c !important;
      }
    `,
  ],
})
export class App {
  authService = inject(AuthService);
  user = this.authService.user;

  logout() {
    this.authService.logout();
  }
}
