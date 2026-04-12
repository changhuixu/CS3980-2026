import { NgOptimizedImage } from '@angular/common';
import { Component, inject, OnInit, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { finalize } from 'rxjs';
import { AuthService } from '../core';

@Component({
  selector: 'app-login',
  imports: [NgOptimizedImage, RouterLink, FormsModule],
  templateUrl: './login.html',
  styleUrl: './login.css',
})
export class Login implements OnInit {
  private route = inject(ActivatedRoute);
  private router = inject(Router);
  private authService = inject(AuthService);
  busy = signal(false);
  username = '';
  password = '';
  loginError = signal(false);

  ngOnInit(): void {
    if (this.authService.user().username) {
      debugger;
      const returnUrl = this.route.snapshot.queryParams['returnUrl'] || '';
      this.router.navigate([returnUrl]);
    }
  }

  login() {
    if (!this.username || !this.password) {
      return;
    }
    this.busy.set(true);
    const returnUrl = this.route.snapshot.queryParams['returnUrl'] || '';
    this.authService
      .login(this.username.trim(), this.password)
      .pipe(finalize(() => this.busy.set(false)))
      .subscribe({
        next: () => {
          this.router.navigate([returnUrl]);
        },
        error: () => {
          this.loginError.set(true);
        },
      });
  }
}
