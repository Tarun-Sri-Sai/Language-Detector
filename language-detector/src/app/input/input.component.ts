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
  minCharacters: number = 30
  private timeoutMillis: number = 500

  constructor(private http: HttpClient, private app: AppService) { }

  detectLanguage(): void {
    if (this.timeout) {
      console.log('Not running because of timeout')
      return
    }

    this.timeout = true

    if (!this.isValidLength()) {
      this.resetTimeout()
      return
    }

    this.http.get<any>(`http://localhost:5000/detect-language?input_text=${this.textInput}`)
      .subscribe({
        next: (response) => {
          this.app.result = `This text is in ${response.language_code}`
        },
        error: (error) => {
          console.error('Error occurred during language detection:', error)
        }
      })

    this.resetTimeout()
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
