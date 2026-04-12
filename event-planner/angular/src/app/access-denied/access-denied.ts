import { ChangeDetectionStrategy, Component, inject } from '@angular/core';
import { AuthService } from '../core';

@Component({
  template: `<div class="container">
    <h2 class="text-danger my-4">Access Denied.</h2>

    <div class="my-5">
      @if (authService.user(); as user) {
        <div class="alert alert-info" role="alert">
          <p class="alert-heading fw-medium">Hello, {{ user.username }},</p>
          <p>
            Your account doesn't have enough permission to view protected content in this website.
          </p>
        </div>
      } @else {
        <div class="alert alert-danger" role="alert">
          <p class="alert-heading fw-medium">Hello,</p>
          <p>You haven't logged in our system or your account doesn't have enough permission.</p>
        </div>
      }
      <button class="btn btn-primary" (click)="authService.logout()">Logout</button>
    </div>
  </div>`,
  styles: [],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class AccessDenied {
  authService = inject(AuthService);
}
