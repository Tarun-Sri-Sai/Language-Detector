import { Component } from '@angular/core'
import { AppService } from '../app.service'
import { HttpClient } from '@angular/common/http'

@Component({
  selector: 'app-input',
  templateUrl: './input.component.html',
  styleUrls: ['./input.component.css']
})
export class InputComponent {
  textInput: string = ''
  private timeout: boolean = false
  minCharacters: number = 20
  private timeoutMillis: number = 250

  constructor(private http: HttpClient, private app: AppService) { }

  detectLanguage(): void {
    if (this.timeout) {
      return
    }

    this.timeout = true

    if (!this.isValidLength()) {
      this.resetTimeout()
      return
    }

    this.computeLanguage()
    this.resetTimeout()
  }

  computeLanguage(): void {
    this.http.put<any>('http://localhost:5000/detect-language', { 'text_input': this.textInput })
      .subscribe({
        next: (response) => {
          this.getLanguageCode()
        },
        error: (error) => {
          console.error("Couldn't post text due to: ", error)
        }
      })
  }

  getLanguageCode(): void {
    this.http.get<any>('http://localhost:5000/detect-language')
    .subscribe({
      next: (response) => {
        this.app.result = response['language_code']
      },
      error: (error) => {
        console.error("Couldn't get language due to: ", error)
      }
    })
  }

  isValidLength(): boolean {
    return this.textInput.trim().replaceAll(/\s+/g, ' ').length >= this.minCharacters
  }

  resetTimeout(): void {
    setTimeout(() => {
      this.timeout = false
    }, this.timeoutMillis)
  }
}
