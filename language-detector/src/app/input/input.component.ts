import { Component } from '@angular/core'
import { AppService } from '../app.service'

@Component({
  selector: 'app-input',
  templateUrl: './input.component.html',
  styleUrls: ['./input.component.css']
})
export class InputComponent {
  constructor(public app: AppService) { }
}
