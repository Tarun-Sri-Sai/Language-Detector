import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <div class="container">
      <div class="row">
        <div class="col-md-6 offset-md-3">
          <app-title></app-title>
          <app-input></app-input>
          <app-result></app-result>
        </div>
      </div>
    </div>

  `,
  styles: [`

  `],
})
export class AppComponent {}

