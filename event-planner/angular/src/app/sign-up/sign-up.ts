import { NgOptimizedImage } from '@angular/common';
import { Component, inject, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';
import { finalize } from 'rxjs';
import { AuthService } from '../core';

@Component({
  selector: 'app-sign-up',
  imports: [NgOptimizedImage, RouterLink, FormsModule],
  templateUrl: './sign-up.html',
  styleUrls: ['./sign-up.css', '../login/login.css'],
})
export class SignUp {
  private authService = inject(AuthService);
  busy = signal(false);
  username = '';
  password = '';
  loginError = signal(false);
  signupSuccess = signal(false);

  signup() {
    if (!this.username || !this.password) {
      return;
    }

    this.busy.set(true);
    this.authService
      .signup(this.username.trim(), this.password)
      .pipe(finalize(() => this.busy.set(false)))
      .subscribe({
        next: () => {
          this.signupSuccess.set(true);
        },
        error: () => {
          this.signupSuccess.set(false);
          this.loginError.set(true);
        },
      });
  }
}
