import { NgOptimizedImage } from '@angular/common';
import { Component, computed, OnInit, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute, ParamMap, RouterLink } from '@angular/router';
import { NgbModal, NgbModalRef } from '@ng-bootstrap/ng-bootstrap';
import { LoadingBar, UiowaRing } from '@uiowa/spinner';
import { finalize, of, switchMap } from 'rxjs';
import { AuthService } from '../../core';
import { Event, EventsService } from '../events.service';

@Component({
  selector: 'app-event-details',
  imports: [RouterLink, UiowaRing, LoadingBar, NgOptimizedImage, FormsModule],
  templateUrl: './event-details.html',
  styleUrl: './event-details.css',
})
export class EventDetails implements OnInit {
  loading = signal(false);
  id = '';
  details = signal<Event | null>(null);
  title = '';
  image = '';
  description = '';
  tags: string[] = [];
  location = '';
  busy = signal(false);
  canUpdate = computed(() => this.authSvc.user().username === this.details()?.creator);

  private modalRef?: NgbModalRef;

  constructor(
    private route: ActivatedRoute,
    private readonly authSvc: AuthService,
    private readonly svc: EventsService,
    private modalService: NgbModal,
  ) {}
  ngOnInit(): void {
    this.route.paramMap
      .pipe(
        switchMap((params: ParamMap) => {
          this.id = params.get('guid') ?? '';
          if (this.id) {
            this.loading.set(true);
            return this.svc.getEventDetails(this.id).pipe(finalize(() => this.loading.set(false)));
          } else {
            return of(null);
          }
        }),
      )
      .subscribe((x) => this.details.set(x));
  }
  open(content: any) {
    this.title = this.details()!.title;
    this.image = this.details()!.image;
    this.description = this.details()!.description;
    this.tags = this.details()!.tags;
    this.location = this.details()!.location;

    this.modalRef = this.modalService.open(content, {
      size: 'lg',
      ariaLabelledBy: 'modal-title',
      backdrop: 'static',
    });
  }

  removeTag(t: string) {
    this.tags = this.tags.filter((x) => x !== t);
  }
  addTag(t: string) {
    if (t && !this.tags.includes(t)) {
      this.tags.push(t);
    }
  }
  update(content: any) {
    this.busy.set(true);
    this.svc
      .updateEventDetails(
        this.id,
        this.title,
        this.image,
        this.description,
        this.tags,
        this.location,
      )
      .pipe(finalize(() => this.busy.set(false)))
      .subscribe((x) => {
        this.details.set(x);
        this.modalRef?.close();
        this.open(content);
      });
  }
}
