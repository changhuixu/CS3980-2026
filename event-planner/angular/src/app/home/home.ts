import { DatePipe } from '@angular/common';
import { Component, inject } from '@angular/core';
import { RouterLink } from '@angular/router';
import { AuthService } from '../core';

@Component({
  selector: 'app-home',
  imports: [RouterLink, DatePipe],
  template: `
    <section class="container">
      @if (user().username) {
        <div class="card mt-4 shadow">
          <h4 class="card-header">Hi {{ user().username }},</h4>
          <div class="card-body">
            <div class="m-2">
              <h6>Your access token is</h6>
              {{ user().access_token }}
            </div>
            <div class="m-2">
              <h6>Token expires at:</h6>
              {{ user().expiry | date: 'medium' }}
            </div>
          </div>
          <div class="card-footer py-3 fs-5">
            To view all the events or add/manage events, please click the
            <a routerLink="events">here</a>.
          </div>
        </div>
      } @else {
        <div class="card mt-4 shadow">
          <h4 class="card-header">You have not logged in</h4>
          <div class="card-body">
            <div class="m-2">Please click <a routerLink="login">here</a> to login.</div>
          </div>
        </div>
      }
    </section>
  `,
  styles: ``,
})
export class Home {
  authService = inject(AuthService);
  user = this.authService.user;
}
